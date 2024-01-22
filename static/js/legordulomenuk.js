(function () {
	let kalkulatorContent = document.getElementById("kalkulatorContent");
	let tableContent = document.getElementById("tableContent");
	let forumContent = document.getElementById("forumContent");
            
	function showMenu(contentId) {
	    hideAllMenus();
	    document.getElementById(contentId).style.display = "block";
	}
            
	function hideMenu(contentId) {
	    document.getElementById(contentId).style.display = "none";
	}
            
	function hideAllMenus() {
	    tableContent.style.display = "none";
	    kalkulatorContent.style.display = "none";
	    forumContent.style.display = "none";
	}
                })();

