document.getElementById("start-button").addEventListener("click", async () => {
 const formContainer = document.getElementById("form-container");
 const storyContainer = document.getElementById("story-container");
 const storyElement = document.getElementById("story");

 // Fetch the words from the backend
 const response = await fetch("http://localhost:5000/get_words");
 const words = await response.json();

 // Create input fields for each word
 formContainer.innerHTML = "";
 words.forEach((word) => {
  const div = document.createElement("div");
  div.className = "input-field";
  // Display the word that needs to be replaced
  const cleanedWord = word.replace(/[<>]/g, "");
  div.innerHTML = `<label for="${cleanedWord}">Replace with:</label> ${cleanedWord}<input type="text" id="${cleanedWord}" />`;
  formContainer.appendChild(div);
 });

 // Add submit button
 const submitButton = document.createElement("button");
 submitButton.innerText = "Submit";
 formContainer.appendChild(submitButton);

 // On submit, send the answers to the backend and display the story
 submitButton.addEventListener("click", async () => {
  const answers = {};
  words.forEach((word) => {
   const cleanedWord = word.replace(/[<>]/g, "");
   answers[word] = document.getElementById(cleanedWord).value;
  });

  const storyResponse = await fetch("http://localhost:5000/submit_answers", {
   method: "POST",
   headers: {
    "Content-Type": "application/json",
   },
   body: JSON.stringify(answers),
  });
  const story = await storyResponse.text();

  // Display the story
  formContainer.style.display = "none";
  storyContainer.style.display = "block";
  storyElement.innerText = story;
 });
});
