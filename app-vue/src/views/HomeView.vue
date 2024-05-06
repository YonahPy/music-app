<template>
  <section>  
    <div class="container_carousel">
      <carousel :items-to-show="3.0" :autoplay="4000" :transition="500" :pause-autoplay-on-hover="true" :wrap-around="true">
        <slide v-for="track in tracksPopularityMonth" :key="track.id" >
          <div class="image_carousel" :style="{'background-image': `url(${track.image})`}">
            <p>{{ track.artist_name }}</p>
            <p>{{ track.name }}</p>
            <ButtonPlayMusic></ButtonPlayMusic>
          </div>
        </slide>

        <template #addons>
          <navigation />
        </template>
      </carousel>  
    </div>
  </section>

  <section>
    <div>
      <h2 class=" my-10 ml-3">Tracks listened to this week</h2>

      <carousel :items-to-show="5.0" :transition="500" :pause-autoplay-on-hover="true" :wrap-around="true">
        <slide v-for="track in tracksListensWeek" :key="track.id">
          <div>
            <div class="">
              <img class="w-100" :src="track.image" alt="">
            </div>
            <p class="text-subtitle-2">{{ track.name }}</p>
          </div>
        </slide>
      </carousel>
    </div>
  </section>

  <section class="d-flex ga-5">
    <div  style="width: 35%;">
      <h2 class="my-10 ml-3">Top Popular Music</h2>
      <div >
        <div v-for="track in tracksMostPopular" :key="track.id" class="d-flex ml-3 align-center">
          
          <div class="image-track-most-popular">
            <img :src="track.image" alt="">
          </div>
          

          <p class="ml-3">{{ track.name }}</p>

          <ButtonAddPlaylist></ButtonAddPlaylist>

          <ButtonPlay></ButtonPlay>
          
        </div>
      </div>
    </div>


    <div style="width: 65%;">
      <h2 class="my-10 ml-3">Genre</h2>
      <div class="genres">

        <div>
          <div class="image-genre">
            <img src="../assets/musical-genre/alternative-rock.jpg" alt="alternative-rock">
          </div>
          <p>Alternative Rock</p>
        </div>

        <div>
          <div class="image-genre">
            <img src="../assets/musical-genre/1-blues-music-harmonica-manuel-schmucker.jpg" alt="blue-music">
          </div>
          <p>Blues</p>
        </div>

        <div>
          <div class="image-genre">
            <img src="../assets/musical-genre/Classical-Music-Classical.jpg" alt="classical-music">
          </div>
          <p>Classical</p>
        </div>

        <div>
          <div class="image-genre">
            <img src="../assets/musical-genre/eletronic.jpg" alt="eletronic-music">
          </div>
          <p>Eletronic</p>
        </div>

        <div>
          <div class="image-genre">
            <img src="../assets/musical-genre/folk.jpg" alt="folk-music">
          </div>
          <p>Folk</p>
        </div>

        <div>
          <div class="image-genre">
            <img src="../assets/musical-genre/grunge.jpg" alt="grunge-music">
          </div>
          <p>Grunge</p>
        </div>

        <div>
          <div class="image-genre">
            <img src="../assets/musical-genre/hard-rock.jpeg" alt="hard-rock-music">
          </div>
          <p>Hard Rock</p>
        </div>

        <div>
          <div class="image-genre">
            <img src="../assets/musical-genre/hip-hop.jpg" alt="hip-hop-music">
          </div>
          <p>Hip Hop</p>
        </div>

        <div>
          <div class="image-genre">
            <img src="../assets/musical-genre/indie.jpg" alt="indie-music">
          </div>
          <p>Indie</p>
        </div>

        <div>
          <div class="image-genre">
            <img src="../assets/musical-genre/jazz.jpg" alt="jazz-music">
          </div>
          <p>Jazz</p>
        </div>

      </div>
    </div>
  </section>

</template>

<script setup lang="ts">
import axios from 'axios'
import { onMounted, ref } from 'vue';
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import ButtonPlayMusic from '@/components/ButtonPlayMusic.vue';
import ButtonAddPlaylist from '@/components/ButtonAddPlaylist.vue';
import ButtonPlay from '@/components/ButtonPlay.vue';


onMounted(() => {
  getTracksPopularityMonth()
  getTracksListensWeek()
  getTracksMostPopular()
  alternativeRockTracks()
  blueTracks()
  classicalTracks()
  folkTracks()
  grungeTracks()
  hardRockTracks()
  hipHopTracks()
  indieTracks()
  eletronicTracks()
  jazzTracks()
})


const tracksPopularityMonth = ref()
const tracksListensWeek = ref()
const tracksMostPopular = ref()
const alternativeRockTrack = ref()
const blueTrack = ref()
const classicalTrack = ref()
const eletronicTrack = ref()
const folkTrack = ref()
const grungeTrack = ref()
const hardRockTrack = ref()
const hipHopTrack = ref()
const indieTrack = ref()
const jazzTrack = ref()

function getTracksPopularityMonth(){
  const params = {
    boost: 'popularity_month',
    limit: '10'
    
  }
  axios.get('tracks/', {params: params})
  .then((response) => {
    tracksPopularityMonth.value =  response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function getTracksListensWeek(){
  const params = {
    order: 'listens_week',
    limit: '20',
    offset: '10'
  }
  axios.get('tracks/', {params:params})
  .then((response) => {
    tracksListensWeek.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function getTracksMostPopular(){
  const params = {
    limit: '10',
    boost: 'popularity_total',
  }
  axios('tracks/', {params:params})
  .then((response) => {
    tracksMostPopular.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function alternativeRockTracks(){
  const params = {
    fuzzytags: 'alternative rock',
  }
  axios('tracks/', {params:params})
  .then((response) => {
    alternativeRockTrack.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function blueTracks(){
  const params = {
    fuzzytags: 'blues',
  }
  axios('tracks/', {params:params})
  .then((response) => {
    blueTrack.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function classicalTracks(){
  const params = {
    fuzzytags: 'classical',
  }
  axios('tracks/', {params:params})
  .then((response) => {
    classicalTrack.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function folkTracks(){
  const params = {
    fuzzytags: 'folk',
  }
  axios('tracks/', {params:params})
  .then((response) => {
    folkTrack.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function grungeTracks(){
  const params = {
    fuzzytags: 'grunge',
  }
  axios('tracks/', {params:params})
  .then((response) => {
    grungeTrack.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function hardRockTracks(){
  const params = {
    fuzzytags: 'hard rock',
  }
  axios('tracks/', {params:params})
  .then((response) => {
    hardRockTrack.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function hipHopTracks(){
  const params = {
    fuzzytags: 'hip hop',
  }
  axios('tracks/', {params:params})
  .then((response) => {
    hipHopTrack.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function indieTracks(){
  const params = {
    fuzzytags: 'indie',
  }
  axios('tracks/', {params:params})
  .then((response) => {
    indieTrack.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function eletronicTracks(){
  const params = {
    fuzzytags: 'eletronic',
  }
  axios('tracks/', {params:params})
  .then((response) => {
    eletronicTrack.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

function jazzTracks(){
  const params = {
    fuzzytags: 'jazz',
  }
  axios('tracks/', {params:params})
  .then((response) => {
    jazzTrack.value = response.data.results
  })
  .catch((error) => {
    console.log(error)
  })
}

</script>

<style scoped>
.container_carousel{
  width: 100%;
  margin: 0 auto;
  height: 400px;
}
.image_carousel{
  height: 400px;
  width: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: flex-end;
}
.image_carousel p,a{
  font-size: 18px;
  font-weight: bold;
}
.image-track-most-popular{
  width: 50px;
}
.image-track-most-popular img{
  width: 100%;
}
.genres{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  padding-right: 40px;
}
.image-genre{
  width: 170px;
  height: 170px;
}
.image-genre img{
width: 100%;
height: 100%;
}
</style>
