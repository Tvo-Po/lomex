<template>
    <div class="card">
        <div class="card__row">
            <div
            :class="actor ? 'card__column-actor card__column-actor_name' :
            genre ? 'card__column-genre card__column-genre_name' :
            director ? 'card__column-director-item card__column-director-wrapper card__column-director_name' : 'card__column'"
            >{{ firstColumn }}</div>
            <div v-if="director && !first" class="card__column-director-wrapper card__column-director_actors card__column_border">
                <div v-if="secondColumn.length > 0" class="card__column-director">
                    <div
                    v-for="(actor, index) in secondColumn"
                    :key='index'
                    class="card__column-director-item"
                    > {{ actor.name }} - {{ actor.movies_count }} {{ getMovieWord(actor.movies_count) }} <br> </div>
                </div>
                <div v-else> - </div>
            </div>
            <div
            v-else
            :class="actor ? 'card__column-actor card__column_border' :
            genre ? 'card__column-genre card__column_border' :
            director ? 'card__column-director_actors card__column_border' : 'card__column'"
            >{{ secondColumn }}
            </div>
            <div v-if="director && !first" class="card__column-director-wrapper card__column-director_movies card__column_border">
                <div v-if="thirdColumn.length > 0">
                    <div
                    v-for="(movie, index) in thirdColumn"
                    :key='index'
                    class="card__column-director-item"
                    > {{ movie.title }} <br> </div>
                </div>
                <div v-else> - </div>
            </div>
            <div
            v-else
            :class="actor ? 'card__column-actor card__column_border' :
            genre ? 'card__column-genre card__column_border' :
            director ? 'card__column-director_movies card__column_border' : 'card__column'"
            >{{ thirdColumn }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'RepresentBlock',
    props: [
        'firstColumn', 'secondColumn', 'thirdColumn',
        'first',
        'actor', 'genre', 'director'
    ],
    methods: {
        getMovieWord(amount) {
            if (amount > 1) {
                return 'Movies'
            }
            else if (amount == 1) {
                return 'Movie'
            }
            else {
                return ''
            }
        }
    }
}
</script>


<style scoped>
    .card{
        display: block;
        background: linear-gradient(47.94deg, #2C3341 19.6%, #313949 77.32%);
        border: 2px solid rgba(49, 57, 73, 0.5);
        box-sizing: border-box;
        box-shadow: -10px -10px 20px rgba(72, 80, 99, 0.26), 10px 10px 20px #262C37;
        border-radius: 12px;
        font-size: 22px;
        font-weight: 700;
        color: rgba(255, 255, 255, 0.65);
        line-height: 27px;
        margin: 25px auto;
        text-align: center;
        padding: 20px 15px;
        width: 1050px;
    }

    .card__row {
        display: flex;
        justify-content: space-around;
        padding: 0 15px;
    }

    .card__column {
        text-align: center;
    }

    .card__column_border {
        border-left: 2px solid rgba(255, 255, 255, 0.45);
    }

    .card__column-actor {
        margin-right: auto;
        text-align: center;
        width: 30%;
        overflow: hidden;
    }

    .card__column-actor_name {
        width: 35%;
    }

    .card__column-genre {
        margin-right: auto;
        text-align: center;
        width: 35%;
        overflow: hidden;
    }

    .card__column-genre_name {
        width: 30%;
    }

    .card__column-director-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 15px;
    }

    .card__column-director-item {
        /* margin-right: auto; */ 
        text-align: center;
        overflow: hidden;
    }

    .card__column-director_name {
        width: 25%;
    }

    .card__column-director_actors {
        width: 40%;
        margin: 0 auto
    }

    .card__column-director_movies {
        width: 30%;
    }

</style>