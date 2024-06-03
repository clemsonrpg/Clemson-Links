function toggleMode(){
    const html = document.documentElement
    html.classList.toggle('light')
    
    const img = document.querySelector('#profile img')

    if(html.classList.contains('light')){
        img.setAttribute('src', './assets/carloslight.jpg')
        img.setAttribute('alt', 'pfp lightmode')
    }
    else{
        img.setAttribute('src', './assets/carlos.png')
        img.setAttribute('alt', 'pfp darkmode')
    }
}