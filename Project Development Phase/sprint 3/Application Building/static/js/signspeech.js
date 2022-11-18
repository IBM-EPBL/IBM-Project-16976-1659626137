var loadFile = function (event) {
  var image = document.getElementById("output");
  image.src = URL.createObjectURL(event.target.files[0]);
  image.onload = function () {
    URL.revokeObjectURL(image.src);
  };
  let t1 = document.getElementById("text");
  // let hidden = element.getAttribute("hidden");
  image.setAttribute("style", "margin-top: 25px;");
  document.getElementById("upfile").setAttribute("style", "display: none");
  t1.removeAttribute("hidden");
};

function refreshWord() {
  var req = new XMLHttpRequest();
  req.open("GET", "/refresh", true);
  req.send();
}

function audio() {
  var req = new XMLHttpRequest();
  req.open("GET", "/audio", true);
  req.send();
}
