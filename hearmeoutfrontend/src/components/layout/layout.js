import React from "react"
import Header from "./header/header"
import Footer from "./footer/footer"
class Layout extends React.Component {
  render(){
    return (
      <>
        <Header />
        <main>{this.props.children}</main>
        <Footer />
      </>
    )
  }
}
export default Layout;