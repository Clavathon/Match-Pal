import React from 'react';
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

const Upload = () => (
  <Form>

    <Form.Group widths='equal'>
      <Form.Field
        id='itemName'
        control={Input}
        label='Item Name'
        placeholder='Macbook Pro 2017'
      />
      <Form.Field
        id='cost'
        control={Input}
        label='Cost'
        placeholder='$2.50 USD'
      />
      <Form.Field
        id='merchant'
        control={Input}
        label='Merchant'
        placeholder='Apple Store'
      />
      <Form.Field
        id='date'
        control={Input}
        label='Date'
        placeholder='08/25/2018'
      />
    </Form.Group>
    <Dropdown 
        placeholder='Categories' 
        selection 
        options={categories} 
      />
    <Button color='blue'>
      <Link to='/search' className='link'>Upload</Link>
    </Button>

  </Form>
)

export default Upload;