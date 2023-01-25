<script >
export default {
  data() {
    return {
      historylist: []
      }
    },
  emits: ['onGetHistoryItems'],
  async mounted() {
    this.getHistoryList()
  },
  props:['historyRefreshWatch'],
  watch:{
    'historyRefreshWatch'(data){
      this.getHistoryList()
    }
  },
  methods: {
    async getHistoryList() {
      const req = await this.$axios.get('calc/histories/all/')
      this.historylist = req.data
    },
    loadGraph(historyId){
      this.$emit('onGetHistoryItems', historyId)
    }
  }
}

</script>

<template>
  <div>
    <table class="table table-hover">
      <tbody>
        <tr class="pointer" v-for="his in historylist" @click="loadGraph(his.id)">
          <td class="align-middle">
            <span 
                class="badge align-middle" 
                :class="{ 'text-bg-dark': his.index.toUpperCase() === 'SPX',
                'text-bg-success': his.index.toUpperCase() === 'WIG20',
                'text-bg-primary': his.index.toUpperCase() === 'DAX',
                }"
                >
                <i class="bi bi-graph-up btn-icon-left"></i>
              {{ his.index.toUpperCase() }}
            </span>
          </td>
          <td class="text-center" >
            <div class="d-inline-block">
              <p class="small-inline-paragraph text-end"><small>Created: {{$moment(his.date_created).format('HH:mm DD.MM.YY')}}</small></p>
              <p class="small-inline-paragraph text-end"><small>Toss count: {{his.count}}</small></p>
              <p class="small-inline-paragraph text-end"><small>Star date: {{$moment(his.starts_from).format('DD.MM.YY')}}</small></p>
            </div>
          </td>
        </tr>
      </tbody>
   </table>
  </div>
</template>
