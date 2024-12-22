document.getElementById("searchBtn").addEventListener("click", function() {
    var ipAddress = document.getElementById("ipAddress").value.trim(); // Get the value of the input field and trim it
    var resultText = document.getElementById("resultText"); // Get the result text element

    // If the IP address input is empty, display a message and stop the function
    if (ipAddress === "") {
        resultText.textContent = "Please enter an IP address."; // Show the error message
        document.getElementById("output").style.display = "block"; // Show the output section
        return;
    }

    // This section can be replaced with an actual API request or search logic
    // For now, a simulated response is displayed after a delay
    setTimeout(function() {
        resultText.textContent = `Results for IP: ${ipAddress} - Country: Iran, City: Tehran`; // Display the result message
        document.getElementById("output").style.display = "block"; // Show the output section
    }, 1500); // Simulated delay of 1.5 seconds
});
