import React from 'react'
import { 
  Button, 
  Form,
  Grid,
  Segment } 
from 'semantic-ui-react'

const Registration = () => (
  <div className='registration-form'>
    <style>{`
      body > div,
      body > div > div,
      body > div > div > div.registration-form {
        height: 100%;
      }
    `}</style>
    <Grid textAlign='center' style={{ height: '100%' }} verticalAlign='middle'>
      <Grid.Column style={{ maxWidth: 450 }}>
        <Form size='large'>
          <Segment>
            <Form.Group widths='equal'>
              <Form.Input fluid placeholder='First Name' />
              <Form.Input fluid placeholder='Last Name' />
            </Form.Group>

            <Form.Input placeholder='Email' />
            <Form.Input
              fluid
              placeholder='Enter Password'
              type='password'
            />
            <Form.Input
              fluid
              placeholder='Re-Enter Password'
              type='password'
            />
            <Button color='blue' fluid size='large'>
              Register
            </Button>
          </Segment>
        </Form>
      </Grid.Column>
    </Grid>
  </div>
)

export default Registration;
