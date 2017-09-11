function showOrgIdDescription() {
    showAndTell(document.getElementById('orgIdDescription'), 'orgIdDescriptionButton');
}

function showApiKeyDescription() {
    showAndTell(document.getElementById('apiKeyDescription'), 'apiKeyDescriptionButton');
}

function showAuthDescription() {
    showAndTell(document.getElementById('authDescription'), 'authDescriptionButton');
}

function showRequestDescription() {
    showAndTell(document.getElementById('requestDescription'), 'requestDescriptionButton');
}

function showDirectDescription() {
    showAndTell(document.getElementById('directDescription'), 'directDescriptionButton');
}


function showAndTell(x, buttonName) {
	if (x != null) {
		if (x.style.display === 'none' || x.style.display === '') {
	        x.style.display = 'block';
	        document.getElementById(buttonName).value = 'hide';
	    } else {
	        x.style.display = 'none';
	        document.getElementById(buttonName).value = '...';
	    }
	}
}