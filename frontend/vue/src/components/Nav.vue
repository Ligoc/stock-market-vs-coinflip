<script>
import Home from '../pages/Home.vue'
import CoinFlip from '../pages/CoinFlip.vue'
//import NotFound from './NotFound.vue'

const routes = {
  '/': Home,
  '/coinflip': CoinFlip
}

export default {
  data() {
    return {
      currentPath: window.location.hash
    }
  },
  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || '/'] || NotFound
    }
  },
  mounted() {
    window.addEventListener('hashchange', () => {
		  this.currentPath = window.location.hash
		})
  },
  methods: {
    isActive(addr) {
      return this.currentPath === addr
    }
  }
}

</script>

<template>
  <div class="px-3 py-2 text-bg-dark">
      <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <a href="/" class="d-flex align-items-center my-2 my-lg-0 me-lg-auto text-white text-decoration-none">
            <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap"><use xlink:href="#bootstrap"></use></svg>
          </a>

          <ul class="nav col-12 col-lg-auto my-2 justify-content-center my-md-0 text-small">
            <li>
              <a href="#" class="nav-link" :class="{ 'text-white' : isActive(''), 'text-secondary':  !isActive('')}">
                <i class="bi bi-house d-block nav-icon"></i>
                Home
              </a>
            </li>
            <li>
              <a href="#/coinflip" class="nav-link" :class="{ 'text-white' : isActive('#/coinflip'), 'text-secondary':  !isActive('#/coinflip')}">
                <i class="bi bi-graph-up-arrow d-block nav-icon"></i>
                Coin Flip
              </a>
            </li>
          </ul>
        </div>
      </div>
  </div>
  <component :is="currentView" />
</template>