import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
# 프론트엔드からの 모든 출처에서의 요청을 허용
CORS(app) 

# Groq 클라이언트 초기화
# API 키는 환경 변수 'GROQ_API_KEY'에서 자동으로 로드됩니다.
try:
    groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    print("Groq client initialized successfully.")
except Exception as e:
    groq_client = None
    print(f"Error initializing Groq client: {e}")

@app.route('/api/convert', methods=['POST'])
def convert_text():
    """
    텍스트 변환을 위한 API 엔드포인트.
    Sprint 1에서는 실제 변환 로직 대신 더미 데이터를 반환합니다.
    """
    data = request.json
    original_text = data.get('text')
    target = data.get('target')

    if not original_text or not target:
        return jsonify({"error": "텍스트와 변환 대상은 필수입니다."}), 400

    # Define prompt templates for each target audience
    prompt_templates = {
        "Upward": """당신은 상사에게 보고하는 어조로 텍스트를 변환하는 전문 비서입니다. 다음 텍스트를 정중하고 격식 있는 보고체로 변환해주세요. 결론부터 명확하게 제시하고, 신뢰성을 강조해주세요.
        ---
        원문: "{text}"
        ---
        변환:""",
        "Lateral": """당신은 타 팀 동료와 협업하는 어조로 텍스트를 변환하는 전문 비서입니다. 다음 텍스트를 친절하고 상호 존중하는 어투로 변환해주세요. 요청 사항과 마감 기한을 명확히 전달하는 협조 요청 형식으로 작성해주세요.
        ---
        원문: "{text}"
        ---
        변환:""",
        "External": """당신은 고객 응대 전문가이며, 고객에게 보내는 어조로 텍스트를 변환합니다. 다음 텍스트를 극존칭을 사용하며, 전문성과 서비스 마인드를 강조하는 형식으로 변환해주세요. 안내, 공지, 사과 등 목적에 부합하게 작성해주세요.
        ---
        원문: "{text}"
        ---
        변환:""",
    }

    if not groq_client:
        return jsonify({"error": "AI 클라이언트가 초기화되지 않았습니다. API 키를 확인해주세요."}), 500

    prompt = prompt_templates.get(target)
    if not prompt:
        return jsonify({"error": "유효하지 않은 변환 대상입니다."}), 400

    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt.format(text=original_text),
                }
            ],
            model="moonshotai/kimi-k2-instruct-0905", # PRD에 명시된 모델 사용
            temperature=0.7,
            max_tokens=500,
        )
        converted_text = chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Groq API 호출 중 오류 발생: {e}")
        return jsonify({"error": f"AI 변환 중 오류가 발생했습니다: {e}. 잠시 후 다시 시도해주세요."}), 500
    
    response_data = {
        "original_text": original_text,
        "converted_text": converted_text,
        "target": target
    }
    
    return jsonify(response_data)


@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# New route to serve other static files (CSS, JS, etc.)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)