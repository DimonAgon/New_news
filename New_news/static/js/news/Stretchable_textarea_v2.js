/**
 * @param {Object} axis Stretchable axes */
function autoStretch(element, axis){

    if (element.classList.contains("auto-Stretchable")){


        while (element.event.inputMode){

            element.rows.length = element.scrollHeight;

        }
    }
}


document.addEventListener("input", autoStretch)


// TODO: make y-stretch function