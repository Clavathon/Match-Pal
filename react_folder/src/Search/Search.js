import React from 'react'
import { Button, Dropdown, Form, Input } from 'semantic-ui-react'
import { Link } from 'react-router-dom'

const categories = [
  {
    text: 'Appliances',
    value: 'appliances',
  },
  {
    text: 'Health & Household',
    value: 'health',
  },
  {
    text: 'Office Supplies',
    value: 'office',
  },
  {
    text: 'Fashion',
    value: 'fashion',
  },
  {
    text: 'Gifts',
    value: 'Gifs',
  },
]

const Search = () => (
  <Form>
    <Button color='blue' textalign='center'>
      <Link to="/upload" className='link'>Upload</Link>
    </Button>
    <Button color='green' textalign='center'>
      <Link to="/login" className='link'>Login</Link>
    </Button>
    <Button color='grey' textalign='center'>
      <Link to="/registration" className='link'>Registration</Link>
    </Button>

    <Form.Group widths='equal'>
      <Form.Field
        id='search'
        control={Input}
        label='Search'
        placeholder='laptops, handbags, dresses, shoes...'
      />
      <Form.Field
        id='Nearby'
        control={Input}
        label='Nearby'
        placeholder='Your location'
      />
    </Form.Group>
    <Dropdown placeholder='Categories' fluid selection options={categories} />
  </Form>
)

export default Search;