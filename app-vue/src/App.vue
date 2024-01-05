<template>
  <div class="grid">
    <header>
      <nav class="superior-bar">
        <div>
          <Search></Search>
        </div>
        <div>
          <button>Tom Johnson</button>
        </div>
    
      </nav>
    </header>
    <aside class="lateral-bar">
      <div class="brand">
        <h2>Jonas App Music</h2>
      </div>
      <div class="items-lateral-bar">
        <h3>Browse Music</h3>
        <div class="div-links-lateral-bar">
            <img src="./assets/icons/icons8-casa-32.png" alt="home">
          <RouterLink to="#">Home</RouterLink>
        </div>
        <div class="div-links-lateral-bar">
          <img src="./assets/icons/icons8-música-50.png" alt="music">
          <RouterLink to="#">Artists</RouterLink>
        </div>
        <div class="div-links-lateral-bar">
          <img src="./assets/icons/icons8-biblioteca-de-música-48.png" alt="music album">
          <RouterLink to="#">Albuns</RouterLink>
        </div>
      </div>
      <div class="items-lateral-bar">
        <h3>Library</h3>
        <div class="div-links-lateral-bar">
          <RouterLink to="#">Favorite Tracks</RouterLink>
        </div>
        <div class="div-links-lateral-bar">
          <RouterLink to="#">Your Playlists</RouterLink>
        </div>
        <div class="div-links-lateral-bar">
          <RouterLink to="#">Recently Played</RouterLink>
        </div>
      </div>
    </aside>
    
    
    <main class="main">
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Search from './components/Search.vue';
</script>


<style >
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  text-decoration: none;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  color: white;
}

p, a{
  font-size: 18px;
}

.grid{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: 80px auto;
  grid-template-areas:
  "lateral-bar superior-bar superior-bar superior-bar"
  "lateral-bar main-content main-content main-content"
  
  
  ;
}
header{
  height: 80px;
}
main{
  grid-area: main-content;
}
.superior-bar{
  grid-area: superior-bar;
  width: 85vw;
  background-color: black;
  display: flex;
  justify-content: flex-end;
  padding: 20px;
  height: 100%;
}
.lateral-bar{
  grid-area: lateral-bar;
  height: 100vh;
  background-color:black ;
  width: 15vw;
  padding: 20px 0px 0px 20px;
  
}
.brand{
  margin-bottom: 40px;
}
.items-lateral-bar{
  margin-bottom: 20px;
}
.div-links-lateral-bar{
  margin-top: 7px;
  margin-left: 10px;
  display: flex;
  align-items: center;
}
.div-links-lateral-bar img{
  width: 18px;
  margin-right: 5px;
}
</style>
