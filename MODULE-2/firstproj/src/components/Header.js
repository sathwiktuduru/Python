import React from'react';

function Header(){
    return(
        <header style={StyleSheet.header}>
         <h1>My Website</h1>
         <nav>
         <ul style={StyleSheet.header}>
            <li>< a  href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href ="#">Contact</a></li>
         </ul>
         </nav>
        </header>
    );
}
const styles={
    header:{
        backgroundColor:'#333',
        color:'white',
        padding:'10px',
        top:'0',
        textAlign:'Center'
    },
    navList:{
        listStyleType:'none',
        padding:0,
        display:'flex',
        justifyContent:'center'
    }
}
export default Header;