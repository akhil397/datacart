document.addEventListener("DOMContentLoaded", function () {
  var editor = CodeMirror.fromTextArea(document.getElementById("id_codes"), {
    lineNumbers: true,
    mode: "python",
    theme: "default",
    indentUnit: 4,
  });
});
