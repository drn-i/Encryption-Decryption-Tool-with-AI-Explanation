document.addEventListener("DOMContentLoaded", function () {
  const algorithmSelect = document.getElementById("algorithm");
  const keyField = document.getElementById("key");
  const keyLabel = document.getElementById("key-label");
  const additionalKeyField = document.getElementById("additional_key");
  const additionalKeyLabel = document.getElementById("additional-key-label");

  const specialAlgos = ["rsa", "elgamal", "diffie-hellman"];
  const keyRequiredAlgos = ["caesar", "vigenere", "hill", "otp", "columnar", "rsa", "diffie-hellman", "elgamal", "aes"];

  function updateFieldVisibility() {
    const selectedAlgo = algorithmSelect.value.toLowerCase();
    const showAdditional = specialAlgos.includes(selectedAlgo);
    const showKey = keyRequiredAlgos.includes(selectedAlgo);

    keyLabel.style.display = showKey ? "block" : "none";
    keyField.style.display = showKey ? "block" : "none";
    keyField.required = showKey;

    additionalKeyLabel.style.display = showAdditional ? "block" : "none";
    additionalKeyField.style.display = showAdditional ? "block" : "none";
  }

  updateFieldVisibility();
  algorithmSelect.addEventListener("change", updateFieldVisibility);

  document.getElementById("crypto-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const algorithm = document.getElementById("algorithm").value;
    const operation = document.getElementById("operation").value;
    const input_text = document.getElementById("input_text").value;
    const key = document.getElementById("key").value;
    const additional_key = document.getElementById("additional_key").value;

    const data = {
      algorithm,
      operation,
      inputText: input_text,
      key,
      additionalKey: additionalKey || null
    };

    try {
      const response = await fetch("http://localhost:9000/crypto", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      const result = await response.json();

      if (response.ok) {
        document.getElementById("output").innerHTML = `
          <strong>Result:</strong> ${result.result}<br><br>
          <strong>Steps:</strong><br>${result.steps.join('<br>')}<br><br>
          <strong>Explanation:</strong><br>${result.explanation}<br><br>
          ${result.image_url ? `<img src="${result.image_url}" alt="AI Explanation" width="300" />` : "<em>No image generated.</em>"}
        `;
      } else {
        document.getElementById("output").textContent = result.detail;
      }
    } catch (error) {
      document.getElementById("output").textContent = "An error occurred. Please try again.";
    }
  });
});