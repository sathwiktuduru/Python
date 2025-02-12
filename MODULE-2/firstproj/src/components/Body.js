import React from 'react';

function Body(){
    return (
        <main style = {StyleSheet.main}>
        <h2>Welcome to My Website</h2>
        <p>This is a simple react application with a structured layout</p>
        </main>
    );
}
const styles={
    main:{
        padding:'20px',
        textAlign:'center'
    }
}
export default Body;