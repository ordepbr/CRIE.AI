// Get input and output elements
const inputText = document.getElementById('input-text');
const generateBtn = document.getElementById('generate-btn');
const outputContainer = document.getElementById('output-container');

// Define API endpoint for AI generator
const apiEndpoint = 'https://api.example.com/generate_animation';

// Function to send text to AI generator API and display generated animation
async function generateAnimation(text) {
  // Show loading spinner
  outputContainer.innerHTML = '<div class="loading-spinner"></div>';
  
  // Send text to API
  const response = await fetch(apiEndpoint, {
    method: 'POST',
    body: JSON.stringify({ text: text })
  });
  
  // Parse response as JSON
  const responseData = await response.json();
  
  // Get URL of generated animation
  const animationUrl = responseData.animation_url;
  
  // Display animation
  outputContainer.innerHTML = `<img src="${animationUrl}" alt="Generated animation">`;
}

// Event listener for generate button
generateBtn.addEventListener('click', () => {
  const inputTextValue = inputText.value;
  if (inputTextValue) {
    generateAnimation(inputTextValue);
  }
});
