<template>
    <div>
        <div>
            <represent-block
            :firstColumn="'Director Name'"
            :secondColumn="'Favourite Actors'"
            :thirdColumn="'Best Movies'"
            :director="true"
            :first="true"
            >
            </represent-block>
        </div>
        <div
        v-for="(director, index) in directors"
        :key='index'>
            <represent-block
            :firstColumn="director.director_name"
            :secondColumn="director.favourite_actors"
            :thirdColumn="director.best_movies"
            :director="true"
            >
            </represent-block>
        </div>
    </div>
</template>

<script>

import RepresentBlock from '@/components/RepresentBlock.vue'

export default {
    name: 'director-representation',
    components: {
        RepresentBlock
    },
    data() {
        return {
            directors: []
        }
    },
    methods: {
        async getDirectors() {
            this.directors = (await this.$api.info.getDirectors()).data.results
        }
    },
    beforeMount() {
        this.getDirectors()
        console.log(this.directors)
    },
}
</script>