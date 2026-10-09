function addTopic() {
    let topic = document.getElementById("topic").value.trim();

    if (!topic) {
        alert("Enter a topic");
        return;
    }

    fetch("http://127.0.0.1:5000/topic", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ topic: topic })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        loadMindMap();
    });
}


function addSubtopic() {
    let topic = document.getElementById("tname").value.trim();
    let subtopic = document.getElementById("subtopic").value.trim();
    let notes = document.getElementById("notes").value.trim();

    if (!topic || !subtopic) {
        alert("Enter topic and subtopic");
        return;
    }

    fetch("http://127.0.0.1:5000/subtopic", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            topic: topic,
            subtopic: subtopic,
            notes: notes
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        loadMindMap();
    });
}


function loadMindMap() {
    fetch("http://127.0.0.1:5000/topics")
        .then(res => res.json())
        .then(data => {
            document.getElementById("output").textContent =
                JSON.stringify(data, null, 4);
        });
}


function deleteTopic() {
    let topic = prompt("Enter topic name:");

    if (!topic) return;

    fetch("http://127.0.0.1:5000/delete/topic", {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ topic: topic })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        loadMindMap();
    });
}


function deleteSubtopic() {
    let topic = prompt("Enter topic name:");
    let subtopic = prompt("Enter subtopic name:");

    if (!topic || !subtopic) return;

    fetch("http://127.0.0.1:5000/delete/subtopic", {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            topic: topic,
            subtopic: subtopic
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        loadMindMap();
    });
}