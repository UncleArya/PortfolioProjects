function confirmDelete(gameID) {
	if (confirm("Are you sure you want to delete this entry?")) {
		document.getElementById("delete-button-" + gameID).setAttribute("href", "/delete?id=" + gameID);
	}
}

function colourMode() {
	if (document.getElementById("colour-mode-selector").getAttribute("data-bs-theme") === "dark") {
		document.getElementById("colour-mode-selector").setAttribute("data-bs-theme", "light");
	} else {
		document.getElementById("colour-mode-selector").setAttribute("data-bs-theme", "dark");
	}
}
