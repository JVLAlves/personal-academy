import {useState, useEffect} from 'react'
import BlogList from './BlogList';

const Home = () => {
 
const [blogs, setBlogs] = useState(null)
const [isPending, setIsPending] = useState(true);
const [error, setError] = useState(null);

useEffect(() => {
setTimeout(() => {
fetch("http://localhost:8000/blogs")
.then(res => {
    if(!res.ok){
        throw Error('Could not fetch the data for that resource')
    }
    return res.json()
})
.then(data => {
    console.log(data)
    setBlogs(data)
    setIsPending(false)
    setError(null)
})
.catch(err => { 
    setError(err.message)
    setIsPending(false)
}) /* Error catching*/

}, 1000)
}, [])

const handleDelete = (id) => {
    const newBlogs = blogs.filter(blog => blog.id !== id);
    setBlogs(newBlogs)
}
    return ( 

        <div className="home">
        {error && <div>{error}</div>}
        {isPending && <div>Loading...</div> }
        {blogs && <BlogList blogs={blogs} title="All Blogs" handleDelete={handleDelete}/>}
        </div>

     );
}
 
export default Home;