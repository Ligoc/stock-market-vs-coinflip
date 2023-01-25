<script>
import StockChart from '../components/StockChart.vue'
import TossSelector from '../components/TossSelector.vue'
import HistoryList from '../components/HistoryList.vue'


export default {  
  data() {
    return {
      formData: null,
      historyId: null,
      historyRefteshInvoker: this.$moment()
    }
  },
    components: {
      StockChart,
      TossSelector,
      HistoryList
    },
  methods: {
    tossSelectorInvoked(data) {
      this.formData = data
    },
    loadHistoryInvoked(historyId) {
      this.historyId = historyId
    }
  }
}
</script>
<template>
    <div class="container-fluid">
    <TossSelector @form-changed="tossSelectorInvoked"/>
    <div class="row pt-3">
      <div class="col">
        <StockChart 
            :inputsWatch="formData" 
            :historyLoadWatch="historyId" 
            @onCalculationCompleated="historyRefteshInvoker=$moment()" 
            charturl="/calc/v2" />
      </div>
    </div>
    <div class="row pt-3 align-items-start">
        <div class="col-4 col-sm-3 col-md-3 col-lg-2 col-xl-2 col-xxl-1 pt-2 
                    offset-8 offset-sm-9 offset-md-9 offset-lg-10 offset-xl-10 offset-xxl-11">    
            <button 
                class="btn btn-dark d-inline btn-full-width" 
                type="button" data-bs-toggle="offcanvas" 
                data-bs-target="#offcanvasHistory" 
                aria-controls="offcanvasHistory">
                    <i class="bi bi-archive nav-icon btn-icon-left"></i>
                    <span>History</span>
            </button>
        </div>
        <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasHistory" aria-labelledby="offcanvasDarkLabel">
            <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvasDarkLabel">History</h5>
                <button @click="retry" class="btn btn-danger d-inline" type="button">
          <i class="bi bi-trash  btn-icon-left"></i>
          <span>Clear</span>
        </button>
            </div>
            <div class="offcanvas-body">
                <HistoryList @onGetHistoryItems="loadHistoryInvoked" :historyRefreshWatch="historyRefteshInvoker" />
            </div>
        </div>
    </div>
  </div>
</template>