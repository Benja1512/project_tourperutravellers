function typeText() {
    const textElement = document.getElementById("text");
    const fullText = textElement.innerText;
    textElement.innerText = ""; // Borrar el texto inicial

    textContainer.style.display = "block"; // Muestra el contenedor de texto cuando comienza la animación

  
    let index = 0;
  
    function showText() {
      if (index < fullText.length) {
        textElement.innerHTML += fullText.charAt(index);
        index++;
        setTimeout(showText, 50); // Ajusta la velocidad de escritura aquí
      } else {
        setTimeout(showVideo, 5000); // Espera 5 segundos antes de iniciar el video
      }
    }
  
    setTimeout(showText, 1000); // Espera 1 segundos antes de iniciar la escritura
  }
  
  function showVideo() {
    document.getElementById("textContainer").style.display = "none"; // Oculta el texto
    document.getElementById("logoContainer").style.display = "none"; // Oculta el logo
    const videoContainer = document.getElementById("videoContainer");
    videoContainer.style.display = "block"; // Muestra el video
    
    const promoVideo = document.getElementById("promoVideo");
    promoVideo.play();
  
    // Llama a la función que muestra el botón justo debajo del video
    showContinueButton();
  }
  
  function showContinueButton() {
    const continueButton = document.getElementById("continueButton");
    continueButton.style.display = "block"; // Muestra el botón centrado debajo del video
  }
  
  function redirectToIndex() {
    window.location.href = "{{ url_for('index') }}";
  }
  
  window.onload = typeText;
  

