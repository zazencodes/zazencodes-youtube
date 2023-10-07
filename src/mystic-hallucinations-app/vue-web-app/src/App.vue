<template>
  <div class="frame" v-if="storyGenerated">
    <StoryView :title="title" :story_html="story_html" />
    <div>
      <img id="story-image" alt="" :src="image_url" />
    </div>
  </div>
  <button class="generate-button" @click="generateMysticHallucination()">
    Generate new story
  </button>
  <div class="footer"></div>
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
      storyGenerated: false,
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
      this.storyGenerated = true;
    },
  },
};
</script>

<style>
/* Button: https://getcssscan.com/css-buttons-examples */
/* Frame: https://codepen.io/chris22smith/pen/PbBwjp */

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
div {
  padding-bottom: 10px;
}
.footer {
  padding-bottom: 100px;
}
#story-image {
  border: 2px solid #4545456c;
  padding: 6px;
  margin: 0 auto;
  border-radius: 2px;
}
.generate-button {
  align-items: center;
  background-color: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 0.25rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: rgba(0, 0, 0, 0.85);
  cursor: pointer;
  display: inline-flex;
  font-family: system-ui, -apple-system, system-ui, "Helvetica Neue", Helvetica,
    Arial, sans-serif;
  font-size: 16px;
  font-weight: 600;
  justify-content: center;
  line-height: 1.25;
  margin: 0;
  min-height: 3rem;
  padding: calc(0.875rem - 1px) calc(1.5rem - 1px);
  position: relative;
  text-decoration: none;
  transition: all 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  width: auto;
}

.generate-button:hover,
.generate-button:focus {
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
  color: rgba(0, 0, 0, 0.65);
}

.generate-button:hover {
  transform: translateY(-1px);
}

.generate-button:active {
  background-color: #f0f0f1;
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
  color: rgba(0, 0, 0, 0.65);
  transform: translateY(0);
}

.frame {
  background-color: rgb(242, 241, 234);
  border: solid 5vmin #eee;
  border-bottom-color: #fff;
  border-left-color: #eee;
  border-radius: 2px;
  border-right-color: #eee;
  border-top-color: #ddd;
  box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.25) inset,
    0 5px 10px 5px rgba(0, 0, 0, 0.25);
  box-sizing: border-box;
  display: inline-block;
  margin: 10vh 10vw;
  /* height: 80vh; */
  padding: 8vmin;
  position: relative;
  text-align: center;
  &:before {
    border-radius: 2px;
    bottom: -2vmin;
    box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.25) inset;
    content: "";
    left: -2vmin;
    position: absolute;
    right: -2vmin;
    top: -2vmin;
  }
  &:after {
    border-radius: 2px;
    bottom: -2.5vmin;
    box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.25);
    content: "";
    left: -2.5vmin;
    position: absolute;
    right: -2.5vmin;
    top: -2.5vmin;
  }
}
</style>
