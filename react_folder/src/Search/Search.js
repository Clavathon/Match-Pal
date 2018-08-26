import React from 'react'
import { Button, Dropdown, Form, Input } from 'semantic-ui-react'

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
    <Button color='blue' textAlign='center'>
      Upload Price
    </Button>
    <Button color='green' textAlign='center'>
      Login
    </Button>
    <Button color='gray' textAlign='center'>
      Register
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