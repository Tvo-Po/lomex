<template>
    <div>
        <div>
            <represent-block
            :firstColumn="'Genre'"
            :secondColumn="'Movies Amount'"
            :thirdColumn="'Average Rating'"
            :genre="true"
            >
            </represent-block>
        </div>
        <div
        v-for="(genre, index) in genres"
        :key='index'>
            <represent-block
            :firstColumn="genre.name"
            :secondColumn="genre.movies_count"
            :thirdColumn="genre.avg_rating ? genre.avg_rating : '-'"
            :genre="true"
            >
            </represent-block>
        </div>
    </div>
</template>

<script>

import RepresentBlock from '@/components/RepresentBlock.vue'

export default {
    name: 'genres-representation',
    components: {
        RepresentBlock
    },
    data() {
        return {
            genres: []
        }
    },
    methods: {
        async getGenres() {
            this.genres = (await this.$api.info.getGenres()).data.results
        }
    },
    beforeMount() {
        this.getGenres()
    },
}
</script>
