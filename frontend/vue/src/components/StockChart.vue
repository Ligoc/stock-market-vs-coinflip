<script >
export default {
  data() {
    return {
      series: [{
            name: 'XYZ MOTORS',
            data: [-10, 41, 35, 51, 49, 62, 69, 91, 148]}],
      chartOptions: {
            chart: {
              type: 'area',
              stacked: false,
              height: 900,
              width: 1024,
              zoom: {
                type: 'x',
                enabled: true,
                autoScaleYaxis: true
              },
              toolbar: {
                autoSelected: 'zoom'
              }
            },
            dataLabels: {
              enabled: false
            },
            markers: {
              size: 0,
            },
            title: {
              text: 'Stock Price Movement',
              align: 'left'
            },
            fill: {
              type: 'gradient',
              gradient: {
                shadeIntensity: 1,
                inverseColors: false,
                opacityFrom: 0.5,
                opacityTo: 0,
                stops: [0, 90, 100]
              },
            },
            yaxis: {
              labels: {
                formatter: function (val) {
                  return parseInt(val) + "$";
                },
              },
              title: {
                text: 'Price'
              },
            },
            xaxis: {
              type: 'datetime',
              labels: {
                datetimeFormatter: {
                  year: 'yyyy',
                  month: 'MM-yyyy',
                  day: 'dd.MM'
                }
              }
            },
            tooltip: {
              shared: false,
              y: {
                formatter: function (val) {
                  return val.toFixed(2) + "$"
                }
              }
            },
            noData: {  
              text: "Loading...",  
              align: 'center',  
              verticalAlign: 'middle',  
              offsetX: 0,  
              offsetY: 0,  
              style: {  
                color: "#000000",  
                fontSize: '14px',  
                fontFamily: "Helvetica"  
              }
            }
          }
        }
  },
  emits: ['onCalculationCompleated'],
  props:['charturl', 'inputsWatch', 'historyLoadWatch'],
  async mounted() {
    this.getApiData()
  },
  watch:{
    'inputsWatch'(data){
      this.getApiData(data)
    },
    'historyLoadWatch'(historyId){
      this.loadfHistoricalData(historyId)
    }
  },
  methods: {
    increment() {
      this.count++
    },

    async getApiData(query) {
      let addr = this.charturl
      if(!query) {
        query = {
          startDate: '2012-02-20',
          tossCount: 100,
          index: 'wig20'
        }
      } 
      addr += "/" + `?startDate=${this.$moment(query.startDate).format('YYYY-MM-DD')}&tossNumber=${query.tossCount}&indexName=${query.index}`
      const req = await this.$axios.get(addr)
      if(req.data) {
        this.$emit('onCalculationCompleated')
        this.series = this.getSeriesData(req.data)
      }
    },

    getSeriesData(dataFromDb) {
      const balance = dataFromDb.map(c => {
        return {'y': c.calucalted_balance, 'x': new Date(c.start_date).getTime()}
      })
      const cumulative = dataFromDb.map(c => {
        return {'y': c.cumulative_difference, 'x': new Date(c.start_date).getTime()}
      })
      return [{ name: 'Toss', data: balance }, { name: 'Acctual market', data: cumulative }]
    },

    async loadfHistoricalData(historyId) {  
      const req = await this.$axios.get('/calc/history/items/' + "?historyId=" + historyId )
      if(req.data) {
        this.series = this.getSeriesData(req.data)
      }
    }
  }
}

</script>

<template>
  <div>
  </div>
  <apexchart type="area" height="600px" width="100%" :options="chartOptions" :series="series"></apexchart>

</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
