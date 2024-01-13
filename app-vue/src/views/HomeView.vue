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

  section
</template>

<script setup lang="ts">
import axios from 'axios'
import { onMounted, ref } from 'vue';
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import ButtonPlayMusic from '@/components/ButtonPlayMusic.vue';

onMounted(() => {
  getTracksPopularityMonth()
  getTracksListensWeek()
})


const tracksPopularityMonth = ref()
const tracksListensWeek = ref()


function getTracksPopularityMonth(){
  const params = {
    boost: 'popularity_month',
    limit: '10'
    
  }
  axios.get('tracks/', {params: params})
  .then((response) => {
    tracksPopularityMonth.value =  response.data.results
    console.log(tracksPopularityMonth.value)
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
    console.log(tracksListensWeek.value)
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


</style>
