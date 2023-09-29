<template>
  <StoryView :title="title" :story_html="story_html" />
  <img alt="" :src="image_url" />
  <button @click="generateMysticHallucination()">Generate new story</button>
</template>

<script>
import StoryView from "./components/StoryView.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    StoryView,
  },
  data() {
    return {
      title: "",
      story_html: "",
      image_url: "",
    };
  },
  methods: {
    async generateMysticHallucination() {
      const resp = await axios.get(
        "http://127.0.0.1:5000/mystic_hallucination/generate"
      );
      this.title = resp.data.title;
      this.story_html = resp.data.story_html;
      this.image_url = resp.data.image_url;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
