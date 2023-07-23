window.addEventListener("load", () => {
    const loader = document.querySelector(".loader");
    loader.classList.add("loader-hidden")
    loader.addEventListener("transitionend", () =>{
        document.body.removeChild("loader");
    })
})

document.getElementById("autoSummarise").addEventListener("click", () => {
    document.getElementById("percentSummarise").checked = false;
})

document.getElementById("percentSummarise").addEventListener("click", () => {
    document.getElementById("autoSummarise").checked = false;
})

document.getElementById("autoSummarise").addEventListener("click", () => {
    document.getElementById("percentage").disabled = true;
})

document.getElementById("percentSummarise").addEventListener("click", () => {
    document.getElementById("percentage").disabled = false;
})