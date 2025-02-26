function getRecommendations() {
    const bookName = document.getElementById("book-name").value;
    const numSuggestions = document.getElementById("num-suggestions").value;
    const suggestionsList = document.getElementById("suggestions-list");

    if (bookName.trim() === "" || numSuggestions <= 0) {
        alert("Please enter a valid book name and number of suggestions.");
        return;
    }

    // Dummy Recommendations (Replace with API or ML model)
    const recommendations = [
        "The Alchemist",
        "To Kill a Mockingbird",
        "1984",
        "Pride and Prejudice",
        "The Great Gatsby",
        "Moby-Dick",
        "Harry Potter Series",
        "The Lord of the Rings"
    ];

    // Shuffle and get required number of suggestions
    const shuffled = recommendations.sort(() => 0.5 - Math.random());
    const selectedBooks = shuffled.slice(0, numSuggestions);

    // Display Recommendations
    suggestionsList.innerHTML = "";
    selectedBooks.forEach(book => {
        let listItem = document.createElement("li");
        listItem.textContent = book;
        suggestionsList.appendChild(listItem);
    });
}
