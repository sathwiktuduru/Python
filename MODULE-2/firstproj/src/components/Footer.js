import React from 'react';

function Footer(){
    return(
        <footer style={styles.footer} >

            <p>&copy; 2024 My Website. All rights reserved.</p>
        </footer>
    );
}
const styles={
    footer:{
        backgroundColor: '#333',
        color: 'white',
        textAlign:'Top',
        padding: '10px',
        width: '100%',
        bottom:0
    }
}
export default Footer;