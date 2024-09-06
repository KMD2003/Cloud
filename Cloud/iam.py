import boto3

def create_vpc():
    ec2 = boto3.client('ec2')

    # Create VPC
    vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc['Vpc']['VpcId']
    print(f"VPC created with ID: {vpc_id}")

    # Tag the VPC
    ec2.create_tags(Resources=[vpc_id], Tags=[{"Key": "Name", "Value": "MyVPC"}])

    # Create Subnet
    subnet = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24')
    subnet_id = subnet['Subnet']['SubnetId']
    print(f"Subnet created with ID: {subnet_id}")

    # Create Internet Gateway
    igw = ec2.create_internet_gateway()
    igw_id = igw['InternetGateway']['InternetGatewayId']
    ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
    print(f"Internet Gateway created and attached: {igw_id}")

    # Create Route Table
    route_table = ec2.create_route_table(VpcId=vpc_id)
    route_table_id = route_table['RouteTable']['RouteTableId']
    print(f"Route Table created with ID: {route_table_id}")

    # Create Route
    ec2.create_route(
        RouteTableId=route_table_id,
        DestinationCidrBlock='0.0.0.0/0',
        GatewayId=igw_id
    )
    print(f"Route added to Route Table: {route_table_id}")

    # Associate Route Table with Subnet
    ec2.associate_route_table(SubnetId=subnet_id, RouteTableId=route_table_id)
    print(f"Route Table {route_table_id} associated with Subnet {subnet_id}")

    return vpc_id, subnet_id, igw_id, route_table_id

if __name__ == "__main__":
    create_vpc()
