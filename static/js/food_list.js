function init() {
    fetch('http://127.0.0.1/food/')
        console.log("API")
        .then(adat => adat.json())
        .then(data => console.log(data)
        )    
}
