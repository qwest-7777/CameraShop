

const openFiltir = () => {
        document.getElementById('filtirnav-2').style.transform = "translateX(0)";
        document.getElementById('filtir-nav-1').style.display = "none";
};

const closeFiltir = () => {
    document.getElementById('filtirnav-2').style.transform = "translateX(-160px)";
    document.getElementById('filtir-nav-1').style.display = "block";
};