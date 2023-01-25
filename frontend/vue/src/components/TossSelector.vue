<script >
import Historylist from './HistoryList.vue'

export default {
  data() {
    return {
      startDate: new Date('2012-02-20T00:00:00.000Z'),
      tossCount: 100,
      index: 'wig20',
    }
  },
  components: {
    Historylist
  },
  emits: ['form-changed'],
  methods: {
    setDate(value) {
      var month = value.getUTCMonth() + 1
      var day = value.getUTCDate()
      var year = value.getUTCFullYear()
      let newdate = year + "-" + month + "-" + day
      this.startDate = newdate
      this.onFormChanged()
    },

    onFormChanged() {
      var data = {  startDate: this.startDate, tossCount: this.tossCount, index: this.index  }
      this.$emit('form-changed', data)
    },
    retry() {
      var data = {  startDate: this.startDate, tossCount: this.tossCount, index: this.index  }
      this.$emit('form-changed', data)
    }
  }
}
</script>

<template>
    <div class="row pt-3 align-items-start">
      <div class="col-8  col-sm-4 col-md-3 col-lg-4 col-xl-4 col-xxl-5 pt-2">
        <datepicker v-model="startDate" :model-value="startDate" @update:model-value="setDate" :format="'dd/MM/yyyy'"></datepicker>
      </div>
      <div class="col-4 col-sm-2  col-md-3 col-lg-3 col-xl-3 col-xxl-3 pt-2">
        <input type="number" class="form-control" placeholder="Number of days" aria-label="City" v-model="tossCount" @change="onFormChanged" >
      </div>
      <div class="col-8 col-sm-3  col-md-3 col-lg-3 col-xl-3 col-xxl-3 pt-2">
        <label class="visually-hidden" for="indexName">Preference</label>
        <select class="form-select" id="indexName" v-model="index" @change="onFormChanged">
          <option value="wig20">WIG20</option>
          <option value="spx">S&P500</option>
          <option value="dax">DAX</option>
        </select> 
      </div>
      <div class="col-4 col-sm-3 col-md-3 col-lg-2 col-xl-2 col-xxl-1  pt-2">
        <button @click="retry" class="btn btn-dark d-inline btn-full-width" type="button">
          <i class="bi bi-coin nav-icon btn-icon-left" style="color: gold;"></i>
          <span>Try again</span>
        </button>
      </div>
    </div>
  
</template>