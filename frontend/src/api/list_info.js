export default function(instance) {
    return {
        getGenres() {
            return instance.get('genres/')
        },
        getActors() {
            return instance.get('actors/')
        },
        getDirectors() {
            return instance.get('directors/?offset=20')
        }
    }
}