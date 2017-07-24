<template>
    <div id="exemplo">
        <table class="table">
            <thead>
                <th><a href="#" @click="sort($event, 'fields.title')">Title</a></th>
                <th><a href="#" @click="sort($event, 'fields.plataform')">Plataform</a></th>
            </thead>
            <tbody>
                <tr v-for="game in lista">
                    <td id="games">{{ game.fields.title }}</td>
                    <td id="games">{{ game.fields.plataform }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        data(){
            return{
                sortDirection: 'desc',
                lista: []
            }
        },
        mounted(){
            this.$http.get("/homepage/games").then( (req) => this.lista = req.data )
        },
        methods:{
            sort(event, campo){
                event.preventDefault()

                if ( this.sortDirection == "desc" )
                {
                    this.sortDirection = "asc"
                }else{
                    this.sortDirection = "desc"
                }

                this.lista = _.orderBy(this.lista, campo, this.sortDirection)

            }
        }
    }
</script>

<style>
    #exemplo{
        color: blueviolet;
    }

    #games{
        color: black;
    }

</style>