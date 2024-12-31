// script.js

// Resize search bar and button dynamically based on window width
function resizeSearchBar() {
    var searchInput = document.getElementById('search-input');
    var searchButton = document.getElementById('search-button');

    if (window.innerWidth < 1000) {
        // Adjust search input and button size
        searchInput.style.width = '80%';
        searchButton.style.width = '15%';
    } else {
        // Reset to default size when width >= 1000px
        searchInput.style.width = 'auto';
        searchButton.style.width = 'auto';
    }
}

// Call the function on resize and initial page load
window.addEventListener('resize', resizeSearchBar);
window.addEventListener('load', resizeSearchBar);
