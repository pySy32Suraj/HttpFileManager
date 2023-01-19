import React from 'react'

import { Home, Header, Sidebar, FilesFolderContianer, DevicesContainer } from './components';


const App = () => {
  
  return (
    <div className='dark:bg-slate-800'>
    
    <Header />
    <Sidebar />
    <Home />

    <DevicesContainer />
    <FilesFolderContianer />
    </div>
  )
}


export default  App;