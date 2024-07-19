async function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    const response = await fetch('/emotionDetector', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: textToAnalyze })
    });

    if (response.status === 400) {
        const errorData = await response.json();
        document.getElementById("system_response").innerText = errorData.error;
    } else {
        const data = await response.json();
        document.getElementById("system_response").innerText = JSON.stringify(data, null, 2);
    }
}
