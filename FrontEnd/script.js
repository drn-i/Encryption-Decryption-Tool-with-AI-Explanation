document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("cryptoForm");
  const algorithmSelect = document.getElementById("algorithm");
  const additionalKeyContainer = document.getElementById("additionalKeyContainer");

  const resultField = document.getElementById("result");
  const explanationField = document.getElementById("explanation");
  const stepsList = document.getElementById("steps");
  const outputContainer = document.getElementById("outputContainer");
  const loading = document.getElementById("loading"); // 🛠️ get the loading div

  // Show/hide additional key for specific algorithms
  algorithmSelect.addEventListener("change", () => {
    const algo = algorithmSelect.value.toLowerCase();
    if (["rsa", "elgamal", "diffehellman"].includes(algo)) {
      additionalKeyContainer.style.display = "block";
    } else {
      additionalKeyContainer.style.display = "none";
    }
  });

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const algorithm = algorithmSelect.value;
    const operation = document.getElementById("operation").value;
    const inputText = document.getElementById("inputText").value;
    const key = document.getElementById("key").value;
    const additionalKey = document.getElementById("additionalKey").value;

    const payload = {
      algorithm,
      operation,
      inputText,
      key,
      additionalKey: additionalKey || null
    };

    try {
      loading.style.display = "block"; // 🛠️ show loading

      const res = await fetch("http://localhost:9090/crypto", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.detail || "Something went wrong");
      }

      resultField.textContent = data.result;
      explanationField.textContent = data.explanation;

      stepsList.innerHTML = "";
      data.steps.forEach((step, idx) => {
        const li = document.createElement("li");
        li.className = "list-group-item";
        li.textContent = step;
        stepsList.appendChild(li);
      });

      outputContainer.style.display = "block";
    } catch (err) {
      alert("Error: " + err.message);
    } finally {
      loading.style.display = "none"; // 🛠️ hide loading whether success or error
    }
  });
});
