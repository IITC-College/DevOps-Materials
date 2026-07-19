import { Link } from 'react-router-dom'
import Seo from '../components/Seo'

export default function NotFound() {
  return <div className="empty-state not-found"><Seo title="Page not found" description="The requested Stryda Athletics page could not be found." /><span>404</span><h1>We lost the trail.</h1><p>The page moved, or maybe it never existed.</p><Link className="button" to="/">Back to home</Link></div>
}
