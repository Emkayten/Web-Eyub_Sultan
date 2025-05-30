// JS Funktionen
document.addEventListener('DOMContentLoaded', () => {
    const burger = document.getElementById('burger');
    const navMenu = document.getElementById('nav-menu');

    burger.addEventListener('click', () => {
        navMenu.classList.toggle('open');
    });
});

function openModal() {
    document.getElementById("newsModal").style.display = "block";
}

function closeModal() {
    document.getElementById("newsModal").style.display = "none";
}

// Modal schließen wenn außerhalb geklickt wird
window.onclick = function(event) {
  var modal = document.getElementById("newsModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

document.getElementById('newsForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    let formData = new FormData(this);

    fetch('/neuigkeit-hinzufuegen/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Neuigkeit erfolgreich gespeichert!');
            location.reload(); // Seite neu laden, um die Neuigkeit anzuzeigen
        } else {
            alert('Fehler beim Speichern!');
        }
    });
});


  
  document.addEventListener("DOMContentLoaded", () => {
    const thumbnails = document.querySelectorAll(".news-thumbnail");
    const mainImage = document.querySelector(".main-news-image");
    const title = document.querySelector(".main-news-text h2");
    const text = document.querySelector(".main-news-text p");
  
    const data = [...thumbnails].map((thumb) => ({
      image: thumb.src,
      title: thumb.alt,
      text: thumb.dataset.text || "Hier könnte Ihr Text stehen",
    }));
  
    thumbnails.forEach((thumb, i) => {
      thumb.addEventListener("click", () => {
        thumbnails.forEach(t => t.classList.remove("active"));
        thumb.classList.add("active");
  
        mainImage.src = data[i].image;
        title.textContent = data[i].title;
        text.textContent = data[i].text;
      });
    });
  });
  
  const thumbnails = document.querySelectorAll('.thumbnail');
  const active = document.getElementById('activeNews');
  const title = document.getElementById('activeTitle');
  const text = document.getElementById('activeText');
  const button = document.getElementById('activeButton');

  thumbnails.forEach((t, i) => {
    t.addEventListener('click', () => {
      active.style.backgroundImage = t.style.backgroundImage;
      title.textContent = t.dataset.title;
      text.textContent = t.dataset.text;
      button.href = t.dataset.link;
    });
  });

  let index = 0;
  setInterval(() => {
    index = (index + 1) % thumbnails.length;
    thumbnails[index].click();
  }, 7000);

  window.onload = function () {
  const canvas = document.getElementById("signature-pad");
  const input = document.getElementById("unterschrift-input");
  const ctx = canvas.getContext("2d");
  let drawing = false;

  canvas.addEventListener("mousedown", e => {
    drawing = true;
    ctx.beginPath();
    ctx.moveTo(e.offsetX, e.offsetY);
  });

  canvas.addEventListener("mousemove", e => {
    if (drawing) {
      ctx.lineTo(e.offsetX, e.offsetY);
      ctx.stroke();
    }
  });

  canvas.addEventListener("mouseup", () => {
    drawing = false;
    input.value = canvas.toDataURL("image/png").split(',')[1];
  });

  canvas.addEventListener("mouseleave", () => {
    if (drawing) {
      drawing = false;
      input.value = canvas.toDataURL("image/png").split(',')[1];
    }
  });

  function touchHandler(e) {
    e.preventDefault();
    const rect = canvas.getBoundingClientRect();
    const touch = e.touches[0];
    if (!drawing) {
      drawing = true;
      ctx.beginPath();
      ctx.moveTo(touch.clientX - rect.left, touch.clientY - rect.top);
    } else {
      ctx.lineTo(touch.clientX - rect.left, touch.clientY - rect.top);
      ctx.stroke();
    }
  }

  canvas.addEventListener("touchstart", touchHandler);
  canvas.addEventListener("touchmove", touchHandler);
  canvas.addEventListener("touchend", () => {
    drawing = false;
    input.value = canvas.toDataURL("image/png").split(',')[1];
  });

  window.clearPad = function () {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    input.value = "";
  };
};


document.addEventListener("DOMContentLoaded", function () {
  var neuigkeitenThumbSlider = new Swiper(".thumb-slider", {
    spaceBetween: 10,
    slidesPerView: 4,
    freeMode: true,
    watchSlidesProgress: true,
  });

  var neuigkeitenMainSlider = new Swiper(".main-slider", {
    spaceBetween: 10,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    thumbs: {
      swiper: neuigkeitenThumbSlider,
    },
  });
});

document.addEventListener("DOMContentLoaded", function() {
  const addBtn = document.getElementById("add-user-btn");
  const modal = document.getElementById("add-user-modal");
  const closeBtn = modal.querySelector(".close-modal");

  addBtn.addEventListener("click", () => {
    modal.style.display = "flex";
  });

  closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  window.addEventListener("click", (e) => {
    if (e.target == modal) {
      modal.style.display = "none";
    }
  });
});
