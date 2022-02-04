const Navbar = () => {
    return ( 
        <nav className="navbar">
            <h1>Swordplay</h1>
            <div className="links">
                <a href="/">Home</a>
                <a href="/chooseClass">Choose a Class</a>
                <a href="/charClass">My Class</a>
                <a href="/enemiesList">Eneminomicon</a>
                <a href="/startFight">Start Now</a>
            </div>
        </nav>

     );
}
 
export default Navbar;