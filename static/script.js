// /static/js/script.js

document.getElementById("uploadForm").addEventListener("submit", function(event) {
    const resumeFile = document.getElementById("resume").files[0];
    if (!resumeFile) {
        alert("Please select a resume file before submitting.");
        event.preventDefault();
    } else {
        // Show loading spinner
        document.getElementById("loadingSpinner").style.display = "block";
    }
});
