async function generatePost() {

    const platform = document.getElementById("platform").value;
    const topic = document.getElementById("topic").value;

    const response = await fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ platform, topic })
    });

    const data = await response.json();

    document.getElementById("result").innerText = data.caption;
}
