<template>
<div id="">
    <table class="table">
        <thead>
            <th>Title</th>
            <th>Plataform</th>
        </thead>
        <tbody>
            <tr v-for="game in lista">
                <td>
                    {{ game.fields.title }}
                </td>
                <td>
                    {{ game.fields.plataform }}
                </td>
            </tr>
        </tbody>
    </table>
</div>
</template>

<script>
export default {
  data(){
      return{
          lista: []
      }
  },
  monted(){
    this.$http.get("/homepage/games").then( (req) => this.lista = req.data )
  }
}
</script>
<style>

</style>
