document.addEventListener('DOMContentLoaded', () => {
    const originalTextInput = document.getElementById('original-text');
    const convertedTextInput = document.getElementById('converted-text');
    const targetAudienceSelect = document.getElementById('target-audience');
    const convertButton = document.getElementById('convert-button');
    const copyButton = document.getElementById('copy-button');
    const currentCharSpan = document.getElementById('current-char');

    // Update character count
    originalTextInput.addEventListener('input', () => {
        currentCharSpan.textContent = originalTextInput.value.length;
    });

    // Handle Convert button click
    convertButton.addEventListener('click', async () => {
        const originalText = originalTextInput.value;
        const target = targetAudienceSelect.value;

        if (!originalText) {
            alert('변환할 텍스트를 입력해주세요.');
            return;
        }

        convertButton.textContent = '변환 중...';
        convertButton.disabled = true;

        try {
            const response = await fetch('http://127.0.0.1:5000/api/convert', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: originalText, target: target }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'API 요청 실패');
            }

            const data = await response.json();
            convertedTextInput.value = data.converted_text;
        } catch (error) {
            console.error('Error during conversion:', error);
            alert(`변환 실패: ${error.message}. 잠시 후 다시 시도해주세요.`);
            convertedTextInput.value = '변환에 실패했습니다.';
        } finally {
            convertButton.textContent = '변환하기';
            convertButton.disabled = false;
        }
    });

    // Handle Copy button click
    copyButton.addEventListener('click', () => {
        convertedTextInput.select();
        convertedTextInput.setSelectionRange(0, 99999); // For mobile devices
        document.execCommand('copy');
        alert('변환된 텍스트가 클립보드에 복사되었습니다!');
    });
});
